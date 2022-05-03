import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import xesmf as xe
import pandas as pd
from flaml import AutoML
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_percentage_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import LocallyLinearEmbedding


def main():
    #exper_loc_avg_yr_avg()
    #exper_yr_avg()
    #exper_pca_yr_avg()
    #exper_lle_yr_avg()
    #exper_water_mask_yr_avg()
    exper_month_avg()


def exper_water_mask_yr_avg():
    factual,cfl,ace, land_mask = water_open_data()
    factual = factual.to_array().transpose("time","lat","lon","variable")

    land_mask = land_mask.to_array()
    land_mask = np.dstack([land_mask]*5)
    land_mask = np.dstack([land_mask]*756)
    land_mask = land_mask.reshape((756,64,41,5))

    land_mask = np.where(land_mask < 0.5, np.NaN, 1)
    factual = np.multiply(factual,land_mask)
    factual = factual.resample(time='AS').mean()
    factual = factual.stack(information=['lat','lon','variable'])
    factual = factual.to_numpy()
    factual = factual[:, ~np.isnan(factual).any(axis=0)]

    X_train, X_test, y_train, y_test = train_test_split(factual,ace,test_size=0.3,shuffle=True, random_state=66)
    y_pred = automl_train_test(X_train, X_test, y_train, y_test)
    prefix = 'automl_water_mask_yr_avg_'
    eval_results(y_test,y_pred, prefix)

def exper_pca_yr_avg():
    factual, cfl, ace = open_data()
    factual = factual.to_array().transpose("time","variable","lat","lon")
    factual = factual.resample(time='AS').mean()
    factual = factual.stack(information=['lat','lon','variable'])
    factual = factual.to_numpy()

    factual = StandardScaler().fit_transform(factual)
    factual = factual.T
    pca = PCA(n_components=63)
    pca.fit_transform(factual)
    factual = pca.components_.T

    X_train, X_test, y_train, y_test = train_test_split(factual,ace,test_size=0.3,shuffle=True, random_state=66)
    y_pred = automl_train_test(X_train, X_test, y_train, y_test)
    prefix = 'automl_pca_yr_avg_'
    eval_results(y_test,y_pred, prefix)

def exper_lle_yr_avg():
    factual, cfl, ace = open_data()
    factual = factual.to_array().transpose("time","variable","lat","lon")
    factual = factual.resample(time='AS').mean()
    factual = factual.stack(information=['lat','lon','variable'])
    factual = factual.to_numpy()

    factual = StandardScaler().fit_transform(factual)
    lle = LocallyLinearEmbedding(n_components=62)
    lle.fit(factual)
    factual = lle.embedding_
    
    X_train, X_test, y_train, y_test = train_test_split(factual,ace,test_size=0.3,shuffle=True, random_state=66)
    y_pred = automl_train_test(X_train, X_test, y_train, y_test)
    prefix = 'automl_lle_yr_avg_'
    eval_results(y_test,y_pred, prefix)

def exper_loc_avg_yr_avg():
    factual, cfl, ace = open_data()

    factual = factual.to_array().transpose("time","variable","lat","lon")
    factual = factual.resample(time='AS').mean()
    factual = factual.stack(location=['lat','lon'])
    factual = factual.mean(dim=["location"])
    factual = factual.to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(factual,ace,test_size=0.3,shuffle=True, random_state=66)
    y_pred = automl_train_test(X_train, X_test, y_train, y_test)
    prefix = 'automl_loc_avg_yr_avg_'
    eval_results(y_test,y_pred, prefix)

def exper_yr_avg():
    factual, cfl, ace = open_data()

    factual = factual.to_array().transpose("time","variable","lat","lon")
    factual = factual.resample(time='AS').mean()
    factual = factual.stack(location=['lat','lon'])
    factual = factual.to_numpy()
    X_train, X_test, y_train, y_test = train_test_split(factual,ace,test_size=0.3,shuffle=True, random_state=66)
    y_pred = automl_train_test(X_train, X_test, y_train, y_test)
    prefix = 'automl_yr_avg_'
    eval_results(y_test,y_pred, prefix)

def exper_month_avg():
    mace,mns = open_monthly_data()
    mace = np.array(mace)
    mns = np.array(mns)
    factual,cfl,ace = open_data()

    factual = factual.to_array().transpose("time","variable","lat","lon")
    factual = factual.stack(information=['lat','lon','variable'])
    factual = factual.to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(factual,ace,test_size=0.3,shuffle=True, random_state=66)
    y_pred = automl_train_test(X_train, X_test, y_train, y_test)
    prefix = 'automl_mth_avg_'
    eval_results(y_test,y_pred, prefix)

def automl_train_test(X_train,X_test,y_train,y_test):
    automl = AutoML()
    automl_settings = {
            "metric": 'rmse',
            "estimator_list": 'auto',
            "task": 'regression',
            "time_budget": 3000,
            "log_file_name": "./automl_factual.log",
        }
    automl.fit(X_train=X_train, y_train=y_train,**automl_settings)
    y_pred = automl.predict(X_test)
    return y_pred

def open_monthly_data():
    mace = open("monthly_activity_ace.csv","r")
    mns = open("monthly_activity_num_storms.csv","r")
    
    mace_contents = mace.readlines()
    mns_contents = mns.readlines()
    
    mace.close()
    mns.close()
    
    mace_dct = []
    mns_dct = []
    
    for i in range(9,len(mace_contents)):
        for j in range(1,13):
            mace_dct.append(float(mace_contents[i].split()[j]))
            mns_dct.append(float(mns_contents[i].split()[j]))
    
    return np.array(mace_dct), np.array(mns_dct)

def open_data():
    #Open the datasets
    factual = xr.open_mfdataset("factual/*.nc")
    cfl = xr.open_mfdataset("eth_cfl/*.nc", join='inner', compat='override')
    
    factual = factual.reduce(np.nansum, dim='expver',keep_attrs=True)
    cfl["lon"] = np.arange(-180,180,2.5)
    factual = factual.rename({"latitude":"lat","longitude":"lon"})
    cfl = cfl.sel(lat=slice(-60,60),lon=slice(-80,20))
    
    #Regrid the factual dataset to be the counterfactual's granularity
    ds_out = xr.Dataset(
        {
            "lat": np.array(cfl["lat"]),
            "lon": np.array(cfl["lon"]),
        }
    )
    regridder = xe.Regridder(factual, ds_out, "bilinear")
    factual = regridder(factual)
    factual = factual.isel(time=slice(0,756)) 
    #factual = factual.isel(time=slice(0,732)) #if monthly
    
    pred_df = pd.read_csv("yearly_activity.csv")
    pred_df = pred_df.loc[pred_df['Year'] >= 1950]
    ace_raw = pred_df['Accumulated Cyclone Energy']
    ace = np.array(ace_raw)
    
    return factual,cfl,ace

def water_open_data():
    #Open the datasets
    factual = xr.open_mfdataset("factual/*.nc")
    cfl = xr.open_mfdataset("eth_cfl/*.nc", join='inner', compat='override')
    
    land_mask = xr.open_dataset("land_mask_gen.nc")
    
    factual = factual.reduce(np.nansum, dim='expver',keep_attrs=True)
    cfl["lon"] = np.arange(-180,180,2.5)
    factual = factual.rename({"latitude":"lat","longitude":"lon"})
    land_mask = land_mask.rename({"latitude":"lat","longitude":"lon"})
    
    ds_out_land = xr.Dataset(
        {
            "lat": np.array(cfl["lat"]),
            "lon": np.array(cfl["lon"]),
        }
    )
    regridder_mask = xe.Regridder(land_mask, ds_out_land, "bilinear",reuse_weights=True)
    land_mask = regridder_mask(land_mask)
    
    cfl = cfl.sel(lat=slice(-60,60),lon=slice(-80,20))
    land_mask = land_mask.sel(lat=slice(-60,60),lon=slice(-80,20))
    
    #Regrid the factual dataset to be the counterfactual's granularity
    ds_out = xr.Dataset(
        {
            "lat": np.array(cfl["lat"]),
            "lon": np.array(cfl["lon"]),
        }
    )
    
    ds_out_land = xr.Dataset(
        {
            "lat": np.array(cfl["lat"]),
            "lon": np.array(cfl["lon"]),
        }
    )
    
    regridder = xe.Regridder(factual, ds_out, "bilinear",reuse_weights=True)
    factual = regridder(factual)
    factual = factual.isel(time=slice(0,756))
    
    
    
    pred_df = pd.read_csv("yearly_activity.csv")
    pred_df = pred_df.loc[pred_df['Year'] >= 1959]
    ace_raw = pred_df['Accumulated Cyclone Energy']
    ace = np.array(ace_raw)

    return factual,cfl,ace, land_mask

def eval_results(y_test,y_pred,pfx):
    print('R^2 Score: ' + str(r2_score(y_test, y_pred)))
    print('RMSE: ' + str(mean_squared_error(y_test,y_pred, squared = False)))
    print('MAE: ' + str(mean_absolute_error(y_test,y_pred)))
    plt.scatter(np.arange(len(y_test)), y_test,label='Observed')
    plt.scatter(np.arange(len(y_test)), y_pred,label='Predicted')
    plt.xlabel('Predicted Season')
    plt.ylabel('Predicted ACE'),
    plt.title('Testing Results')
    plt.legend()
    plt.savefig(pfx+'pred_v_act.png')
    plt.show()
    plt.scatter(y_test,y_pred)
    plt.xlabel('Observed')
    plt.ylabel('Predicted')
    plt.title('Testing Results - Predicted v Observed')
    plt.savefig(pfx+'tseries.png')
    plt.show()
    plt.scatter(y_test, y_test-y_pred)
    plt.plot(y_test,np.zeros(len(y_test)))
    plt.xlabel('Observed')
    plt.ylabel('Residual from Predicted')
    plt.title('Testing Results - Residual')
    plt.savefig(pfx+'residuals.png')
    plt.show()

if __name__ == '__main__':
    main()