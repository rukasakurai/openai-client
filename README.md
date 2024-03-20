[Managed ID Version is here](https://github.com/07JP27/openai-client/tree/managed-id)

# Simple ChatGPT client
It is a Python application that serves as the frontend for Azure Open AI's ChatGPT.
It is assumed to be deployed on Azure App Service.

![image](https://github.com/07JP27/openai-client/assets/11060273/39fe32fd-3046-431a-8d39-36d64130faa8)

# 1. Deploy App Service
Deploy Python Stack Web Apps

## TODO: Note about tested with which version
I am testing with 3.12 now, and on Japan East.

# 2.Deploy this application
Web Apps > Deployment Center > Setting
- Source : External Git
- Repository : https://github.com/07JP27/openai-client
- Branch : main
- Repository Type : Public

![image](https://github.com/07JP27/openai-client/assets/11060273/ddb1893c-6384-47a2-bf17-ebe7b90e2139)

And click Save button.

# 3.Set startup command
Web Apps > Configuration > General settings > Startup Command

```
python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
```

![image](https://github.com/07JP27/openai-client/assets/11060273/32fe52a8-15d6-40e2-80ea-10dae3e6457b)

And click Save button.

# 4. Set Enviroment variables
Web Apps > Configuration > Application settings

- OPENAI_API_ENDPOINT : Your Azure Open AI API endpoint URL
- OPENAI_API_KEY : Your Azure Open AI API key
- OPENAI_API_VERSION : API Vearsion (2023-03-15-preview)
- OPENAI_ENGINE : The model name you deployed

![image](https://github.com/07JP27/openai-client/assets/11060273/a34ffd2d-f044-4202-be09-fe04ad6f7c79)

And click Save button.

## TODO: Clarify app settings or connection strings
I used App settings.

I think it might be only
AZURE_APIM_ENDPOINT = os.getenv("AZURE_APIM_ENDPOINT")

## TODO: Steps to create APIM
Deployed APIM Developer tier to Japan East

## Debugging

The following occurs when settings such as AZURE_OPENAI_DEPLOYMENT are not in place
```
2024-03-20T23:16:32.259427359Z     st.sidebar.text("Engine???"+AZURE_OPENAI_DEPLOYMENT)
2024-03-20T23:16:32.259436559Z                     ~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~
2024-03-20T23:16:32.259439859Z TypeError: can only concatenate str (not "NoneType") to str
```


# Access and Enjoy your private ChatGPT!
If you want to set up authentication to client app, Please refer to following document.
https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service
