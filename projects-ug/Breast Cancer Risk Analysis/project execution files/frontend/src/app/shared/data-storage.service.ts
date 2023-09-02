import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable, OnInit } from '@angular/core';
import { exhaustMap, map, take, tap } from 'rxjs/operators';
import { AuthService } from '../auth/auth.service';
import { DashboardService } from '../dashboard/dashboard.service';
import { Member } from '../dashboard/member.model';

@Injectable({ providedIn: 'root' })
export class DataStorageService implements OnInit {
  constructor(
    private http: HttpClient,
    private dashboardService: DashboardService,
    private authService: AuthService
  ) {}

  ngOnInit() {}

  storeMembers() {
    const members = this.dashboardService.getMembers();
    const uid = this.authService.uid;
    this.http
      .put(
        'https://finalyearprojectapp-30924-default-rtdb.asia-southeast1.firebasedatabase.app/memberData/' +
          uid +
          '/members.json',
        members
      )
      .subscribe((response) => {
        console.log(response);
      });
  }

  loadMembers() {
    const uid = this.authService.uid;

    return this.http
      .get<Member[]>(
        'https://finalyearprojectapp-30924-default-rtdb.asia-southeast1.firebasedatabase.app/memberData/' +
          uid +
          '/members.json'
      )
      .pipe(
        map((members) => {
          return members.map((member) => {
            return {
              ...member,
              dob: new Date(member.dob),
            };
          });
        }),
        tap((members) => {
          this.dashboardService.setMembers(members);
        })
      );
  }
}
