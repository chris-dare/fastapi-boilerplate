# Core API for Oremi
This API is built on FastAPI

## Launching
```bash
docker-compose build
docker-compose up -d
```

## Deployment
### Deploying to Elastic beanstalk (EB2)
Set up the app on EB2 (summary)
```bash
eb init
eb create
eb deploy
```
You'll need to add the environment variables for the application. See .env.sample for samples.
This [guide](https://aws.amazon.com/premiumsupport/knowledge-center/elastic-beanstalk-pass-variables/) will help you configure environment variables in EB2.


This is code I'm writing for a school project. I thought it will be of public benefit so I'm writing the foundations of it and making it public. Once it reaches stability, I will make a private fork. 

** My Archilles heels is not documenting code until it runs. So bear with me.
