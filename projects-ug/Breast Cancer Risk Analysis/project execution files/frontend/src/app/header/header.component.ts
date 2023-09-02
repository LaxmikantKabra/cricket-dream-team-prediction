import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { AuthService } from '../auth/auth.service';
import { HeaderService } from './header.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
})
export class HeaderComponent implements OnInit, OnDestroy {
  constructor(
    private headerService: HeaderService,
    private authService: AuthService,
    private router: Router
  ) {}

  public found = true;
  iscollapsed = true;
  isAuthenticated = false;
  public emailId: string = '';
  subscription: Subscription;
  subscription2: Subscription;
  subscription3: Subscription;
  ngOnInit(): void {
    this.subscription = this.headerService.headerToggle.subscribe((next) => {
      this.found = next;
    });
    this.subscription2 = this.headerService.emailUpdate.subscribe((email) => {
      this.emailId = email;
      this.headerService.email = this.emailId;
    });
    this.subscription3 = this.authService.user.subscribe((user) => {
      this.isAuthenticated = !!user;
    });
    if (this.authService.bcriskuser) {
      this.emailId = this.authService.bcriskuser.email;
      this.headerService.email = this.emailId;
    }
  }

  onLogout() {
    this.authService.logout();
    this.router.navigate(['/auth']);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
    this.subscription2.unsubscribe();
    this.subscription3.unsubscribe();
  }
}
