import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { RiskAssessmentComponent } from './risk-assessment/risk-assessment.component';
import { HomeComponent } from './home/home.component';
import { AppRoutingMoule } from './app-routing.module';
import { AssessmentResultComponent } from './assessment-result/assessment-result.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MemberListComponent } from './dashboard/member-list/member-list.component';
import { MemberStartComponent } from './dashboard/member-start/member-start.component';
import { MemberEditComponent } from './dashboard/member-edit/member-edit.component';
import { FormsModule } from '@angular/forms';
import { AuthComponent } from './auth/auth.component';
import { LoadingSpinnerComponent } from './shared/loading-spinner/loading-spinner.component';
import { OneMemberComponent } from './dashboard/member-list/one-member/one-member.component';
import { MemberDetailComponent } from './dashboard/member-detail/member-detail.component';
import { AuthInterceptorService } from './auth/auth-interceptor.service';
import { AlertComponent } from './shared/alert/alert.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    RiskAssessmentComponent,
    HomeComponent,
    AssessmentResultComponent,
    NotFoundComponent,
    DashboardComponent,
    MemberListComponent,
    MemberStartComponent,
    MemberEditComponent,
    AuthComponent,
    LoadingSpinnerComponent,
    OneMemberComponent,
    MemberDetailComponent,
    AlertComponent,
  ],
  imports: [BrowserModule, AppRoutingMoule, HttpClientModule, FormsModule],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptorService,
      multi: true,
    },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
