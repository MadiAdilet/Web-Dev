import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Album } from '../models/album';
import { Photo } from '../models/photo';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  private apiUrl = 'https://jsonplaceholder.typicode.com';

  constructor(private http: HttpClient) {
    console.log('AlbumService constructor called');
  }

  getAlbums(): Observable<Album[]> {
    console.log('getAlbums called, making HTTP request to:', `${this.apiUrl}/albums`);
    // Try using fetch instead of HttpClient
    return new Observable((observer) => {
      fetch(`${this.apiUrl}/albums`)
        .then(response => response.json())
        .then(data => {
          console.log('Fetch response:', data);
          observer.next(data);
          observer.complete();
        })
        .catch(error => {
          console.error('Fetch error:', error);
          observer.error(error);
        });
    });
  }

  getAlbum(id: number): Observable<Album> {
    return this.http.get<Album>(`${this.apiUrl}/albums/${id}`);
  }

  getAlbumPhotos(id: number): Observable<Photo[]> {
    return this.http.get<Photo[]>(`${this.apiUrl}/albums/${id}/photos`);
  }

  updateAlbum(album: Album): Observable<Album> {
    return this.http.put<Album>(`${this.apiUrl}/albums/${album.id}`, album);
  }

  deleteAlbum(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/albums/${id}`);
  }
}