import { Injectable } from '@angular/core';
import {
  ActivatedRouteSnapshot,
  Resolve,
  RouterStateSnapshot,
} from '@angular/router';

import { DataStorageService } from '../shared/data-storage.service';
import { DashboardService } from './dashboard.service';
import { Member } from './member.model';

@Injectable({ providedIn: 'root' })
export class MembersResolverService implements Resolve<Member[]> {
  constructor(
    private dataStorageService: DataStorageService,
    private dashboardService: DashboardService
  ) {}
  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    const members = this.dashboardService.getMembers();
    if (members.length === 0) {
      return this.dataStorageService.loadMembers();
    } else {
      return members;
    }
  }
}
