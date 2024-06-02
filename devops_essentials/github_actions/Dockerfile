# Use a base image for oficial node.js
FROM node:14

# create and establish work directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# copy the code of app
COPY . .

# Expose the port that app will use
EXPOSE 8080

# command to execute app
CMD ["node", "app.js"]