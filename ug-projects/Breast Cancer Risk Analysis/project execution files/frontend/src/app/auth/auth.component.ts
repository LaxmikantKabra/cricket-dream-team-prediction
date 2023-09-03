import { Component, ComponentFactoryResolver } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { HeaderService } from '../header/header.service';

import { AuthService, AuthResponseData } from './auth.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
})
export class AuthComponent {
  constructor(
    private authService: AuthService,
    private router: Router,
    private headerService: HeaderService  ) {}

  isLoginMode = true;
  isLoading = false;
  error: string = null;

  onSwitchMode() {
    this.isLoginMode = !this.isLoginMode;
  }

  onSubmit(form: NgForm) {
    if (!form.valid) {
      return;
    }
    const email = form.value.email;
    const password = form.value.password;

    let authObs: Observable<AuthResponseData>;

    this.isLoading = true;
    if (this.isLoginMode) {
      authObs = this.authService.login(email, password);
    } else {
      authObs = this.authService.signup(email, password);
    }

    authObs.subscribe(
      (resData) => {
        /* resData -> variable for Response Data */
        // console.log(resData);
        this.isLoading = false;
        this.headerService.emailUpdate.next(resData.email);
        this.router.navigate(['/my_dashboard']);
      },
      (errorMessage) => {
        this.error = errorMessage;
        console.log(errorMessage);
        this.isLoading = false;
      }
    );
    form.reset();
  }
  onHandleError() {
    this.error = null;
  }

  onReturn() {
    this.router.navigate(['./home']);
  }
}
