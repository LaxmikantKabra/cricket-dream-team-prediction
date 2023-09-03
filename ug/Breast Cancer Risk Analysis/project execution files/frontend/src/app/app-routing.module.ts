import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AssessmentResultComponent } from './assessment-result/assessment-result.component';
import { AuthComponent } from './auth/auth.component';
import { AuthGuard } from './auth/auth.guard';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MemberDetailComponent } from './dashboard/member-detail/member-detail.component';
import { MemberEditComponent } from './dashboard/member-edit/member-edit.component';
import { MembersResolverService } from './dashboard/member-resolver.service';
import { MembersResolverService2 } from './dashboard/member-resolver2.service';
import { MemberStartComponent } from './dashboard/member-start/member-start.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { RiskAssessmentComponent } from './risk-assessment/risk-assessment.component';

const appRoutes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  {
    path: 'my_dashboard',
    component: DashboardComponent,
    canActivate: [AuthGuard],
    children: [
      {
        path: '',
        component: MemberStartComponent,
        resolve: [MembersResolverService2],
      },
      {
        path: 'new',
        component: MemberEditComponent,
        resolve: [MembersResolverService2],
      },
      {
        path: ':id',
        component: MemberDetailComponent,
        resolve: [MembersResolverService],
      },
      {
        path: ':id/edit',
        component: MemberEditComponent,
        resolve: [MembersResolverService],
      },
    ],
  },
  {
    path: 'risk_assessment',
    component: RiskAssessmentComponent,
    // canActivate: [AuthGuard],
  },
  {
    path: 'assessment_result',
    component: AssessmentResultComponent,
    // canActivate: [AuthGuard],
  },
  { path: '404-page-not-found', component: NotFoundComponent },
  { path: 'auth', component: AuthComponent },
  { path: '**', redirectTo: '/404-page-not-found' },
];

@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule],
})
export class AppRoutingMoule {}
