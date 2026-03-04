import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { AlbumService } from '../services/album.service';
import { Album } from '../models/album';
import { Location } from '@angular/common';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  album: Album | null = null;
  loading = true;
  editedTitle = '';

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService,
    private router: Router,
    private location: Location
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.albumService.getAlbum(id).subscribe({
      next: (data) => {
        this.album = data;
        this.editedTitle = data.title;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading album', err);
        this.loading = false;
      }
    });
  }

  saveTitle(): void {
    if (!this.album) return;
    const updatedAlbum = { ...this.album, title: this.editedTitle };
    this.albumService.updateAlbum(updatedAlbum).subscribe({
      next: () => {
        if (this.album) this.album.title = this.editedTitle;
        alert('Album title updated!');
      },
      error: (err) => console.error('Update failed', err)
    });
  }

  goBack(): void {
    this.location.back();
  }
}