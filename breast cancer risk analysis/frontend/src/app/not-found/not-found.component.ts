import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HeaderService } from '../header/header.service';

@Component({
  selector: 'app-not-found',
  templateUrl: './not-found.component.html',
  styleUrls: ['./not-found.component.css'],
})
export class NotFoundComponent implements OnInit {
  constructor(private headerService: HeaderService, private router: Router) {}

  ngOnInit() {
    this.headerService.headerToggle.next(false);
  }

  toHome() {
    this.router.navigate(['/home']);
    this.headerService.headerToggle.next(true);
  }
}
