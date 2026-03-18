import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { AlbumService } from '../services/album.service';
import { Album } from '../models/album';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  albums: Album[] = [];
  loading = true;

  constructor(private albumService: AlbumService) {
    console.log('AlbumsComponent constructor called');
  }

  ngOnInit(): void {
    console.log('AlbumsComponent ngOnInit called');
    this.albumService.getAlbums().subscribe(
      (data) => {
        console.log('Albums loaded:', data);
        this.albums = data;
        this.loading = false;
      },
      (err) => {
        console.error('Failed to load albums', err);
        this.loading = false;
      }
    );
  }

  deleteAlbum(id: number): void {
    this.albumService.deleteAlbum(id).subscribe({
      next: () => {
        this.albums = this.albums.filter(album => album.id !== id);
      },
      error: (err) => console.error('Delete failed', err)
    });
  }
}

