

## Running autogen after docker is running

for running the documentation
```
cd ~/apis/autogen/website
yarn install --frozen-lockfile --ignore-engines
pydoc-markdown
python process_notebooks.py render
yarn start --host 0.0.0.0 --port 3000
```

for runing AutogenStudio
```
cd ~/apis/autogen/samples/apps/autogen-studio
pip install -e .
yarn install
yarn build

yarn start --host 0.0.0.0 --port 8082
```



## Other info
cd apis/autogen
pip install -e .[test,teachable,lmm,retrievechat,mathchat,blendsearch]

cd samples/apps/autogen-studio
pip install -e .
autogenstudio ui --host 0.0.0.0 --port 8081

cd samples/apps/autogen-studio/frontend
yarn develop

yarn start --host 0.0.0.0

yarn dev
//
yarn install
yarn build
ws2