import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { AuthResponseData } from '../auth/auth.service';
import { Member } from '../dashboard/member.model';

@Injectable({ providedIn: 'root' })
export class RiskAssessmentService implements OnInit {
  assessMember: Member;
  isMember: boolean = false;

  constructor(
    private http: HttpClient,
  ) {}

  ngOnInit() {}

  setMember(member: Member) {
    this.assessMember = member;
    this.isMember = true;
  }

  predictRisk(data: any) {
    console.log(data);
    return this.http
      .post<AuthResponseData>('http://127.0.0.1:8000/api/prisk/', { data })
      .pipe(catchError(this.handleError));
  }

  private handleError(errorRes: HttpErrorResponse) {
    let errorMessage = 'An unknown error occured';
    if (!errorRes.error || !errorRes.error.error) {
      return throwError(errorMessage);
    } else throwError(errorRes.error);
  }
}
