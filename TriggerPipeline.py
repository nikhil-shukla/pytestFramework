import requests
from utilities.ConfigurationReader import read_config


def trigger_jenkins_pipeline(job_name, parameters=None):
    jenkins_url = "http://localhost:8080/"
    auth = ('nikhil','11f85a12738900aa40a4a9cba35d6be9c2')

    build_url = f"{jenkins_url}/job/{job_name}/build"
    data = {'parameter': parameters} if parameters else None

    response = requests.post(build_url, auth=auth, data=data)

    if response.status_code == 201:
        print(f"Pipeline {job_name} triggered successfully!")
    else:
        print(f"Failed to trigger pipeline {job_name} - Status code: {response.status_code}")


if __name__ == "__main__":
    trigger_jenkins_pipeline('newPipeline', parameters={'BROWSER':'chrome-headless','ENV':'qa'})
