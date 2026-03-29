# Deployment Guide for Meal Planning MVP Application

## Prerequisites
Before deploying the Meal Planning MVP application, ensure you have the following prerequisites installed:
- Node.js (version X.X.X or higher)
- npm or yarn package manager
- Docker (if using Docker deployment)

## Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/naphekiet-gif/Meal-planning-mvp.git
   cd Meal-planning-mvp
   ```
2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```
3. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with your configuration settings.

## Building for Production
To build the application for production:
```bash
npm run build
# or
yarn build
```

## Deployment Options
### Vercel
1. Sign up/log in to [Vercel](https://vercel.com).
2. Import your repository from GitHub.
3. Configure the build settings if necessary (default settings usually work).
4. Click on the "Deploy" button.

### Netlify
1. Sign up/log in to [Netlify](https://www.netlify.com).
2. Click on "New site from Git" and connect the GitHub repository.
3. Set the build command to `npm run build` and publish directory to `build`.
4. Click on "Deploy site".

### Docker
1. Create a Dockerfile in the root of your project:
   ```dockerfile
   FROM node:X.X.X
   WORKDIR /app
   COPY . .
   RUN npm install
   RUN npm run build
   EXPOSE 3000
   CMD ["npm", "start"]
   ```
2. Build the Docker image:
   ```bash
   docker build -t meal-planning-mvp .
   ```
3. Run the Docker container:
   ```bash
   docker run -p 3000:3000 meal-planning-mvp
   ```

## Post-Deployment Steps
- Verify that the application is running by navigating to your deployment URL.
- Check for any errors in the console logs.

## Troubleshooting Guidance
- If you encounter any issues, check the following:
  - Ensure all dependencies are installed correctly.
  - Review the console logs for error messages.
  - Double-check your environment variables in the `.env` file.
  - For Docker, ensure that the correct ports are exposed and mapped.
  - Check the documentation for the chosen deployment platform for common issues.

---