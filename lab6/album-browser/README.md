# Album Browser

An Angular application for browsing albums and their photos using the JSONPlaceholder API.

## Features

- Browse a list of albums
- View album details and edit titles
- View photos for each album in a responsive grid
- Navigation between different views
- CRUD operations (Create, Read, Update, Delete) for albums

## Technologies Used

- Angular 21
- Angular Router for navigation
- Angular HttpClient for API calls
- RxJS for reactive programming
- JSONPlaceholder API for mock data

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn
- Angular CLI

### Installation

1. Clone the repository
2. Navigate to the project directory:
   ```bash
   cd lab6/album-browser
   ```
3. Install dependencies:
   ```bash
   npm install
   ```

### Running the Application

Start the development server:
```bash
ng serve
```

The application will be available at `http://localhost:4200/`.

### Building for Production

To build the project for production:
```bash
ng build --configuration production
```

The build artifacts will be stored in the `dist/` directory.

## API Information

This application uses the JSONPlaceholder API:
- Base URL: https://jsonplaceholder.typicode.com
- Albums endpoint: GET /albums
- Single album: GET /albums/:id
- Album photos: GET /albums/:id/photos
- Update album: PUT /albums/:id
- Delete album: DELETE /albums/:id

## Project Structure

```
src/
├── app/
│   ├── models/
│   │   ├── album.ts
│   │   └── photo.ts
│   ├── services/
│   │   └── album.service.ts
│   ├── home/
│   ├── about/
│   ├── albums/
│   ├── album-detail/
│   ├── album-photos/
│   ├── app.routes.ts
│   ├── app.config.ts
│   ├── app.ts
│   ├── app.html
│   └── app.css
└── ...
```

## Routes

- `/` - Redirects to `/home`
- `/home` - Welcome page
- `/about` - About page
- `/albums` - List of all albums
- `/albums/:id` - Album details
- `/albums/:id/photos` - Photos for an album

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
