# Base image from internal Harbor (mirrors docker.io/library/node)
FROM harbor.haivivi.cn/library/node:20-alpine

WORKDIR /app

COPY package.json index.js ./

ENV PORT=8080
EXPOSE 8080

USER node

CMD ["node", "index.js"]
