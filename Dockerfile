FROM node:16-alpine as build

COPY ./web/app /web/app

WORKDIR /web/app

ARG REACT_APP_DRAW_TOKEN
ENV REACT_APP_DRAW_TOKEN $REACT_APP_DRAW_TOKEN

RUN npm install

RUN npm run build

FROM python:3.7.9-alpine as prod

RUN apk add --no-cache --update postgresql-dev musl-dev gcc

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /backend

COPY ./api/ ./api/
COPY ./giveaway/ ./giveaway/
COPY ./*.py ./
COPY ./*.sh ./
COPY --from=build /web/app/build ./web/app

EXPOSE $PORT

ENTRYPOINT [ "sh", "runserver.sh" ]
