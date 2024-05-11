FROM node:14

WORKDIR /app

CMD ["node", "app.js"]

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "node", "app.js" ]
