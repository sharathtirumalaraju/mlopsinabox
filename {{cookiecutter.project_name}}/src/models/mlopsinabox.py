import os
import mlflow
from configparser import ConfigParser
import dvc.api

os.chdir('../../')
file_path = os.getcwd()

file='config.ini'
config=ConfigParser()
config.read(file_path+'/'+file)

#mlflow tracking uri
track= config['mlflow_uri']['tracking_uri']
mlflow.set_tracking_uri(track)

#retreives data from dvc storage
def get_data(data,version):
  path = config['dvc_remote']['git_dvc']+data
  repo = config['git_repo']['git_uri']
  rev = version
  data_url = dvc.api.get_url(path= path,repo= repo,rev=rev)
  return data_url

#runs your experiments
def log_model(experiment, model, metrics, params):
  mlflow.set_experiment(experiment)
  with mlflow.start_run(run_name=experiment) as run:
      mlflow.log_param("params", params )
      mlflow.log_metric("Accuracy", metrics)
      mlflow.sklearn.log_model(model,"model")
      mlflow.end_run()
