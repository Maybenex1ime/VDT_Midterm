FROM node:18.2.0-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json files separately to utilize layer caching
COPY package.json package-lock.json ./

RUN npm install

# Copy the entire application code to the container
COPY . .

# Build the application
RUN npm run build

EXPOSE 3000

# Specify the default command to run the application
CMD ["npm", "start"]
