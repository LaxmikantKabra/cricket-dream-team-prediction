import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { DataStorageService } from 'src/app/shared/data-storage.service';

import { DashboardService } from '../dashboard.service';
import { Member } from '../member.model';

@Component({
  selector: 'app-member-list',
  templateUrl: './member-list.component.html',
  styleUrls: ['./member-list.component.css'],
})
export class MemberListComponent implements OnInit, OnDestroy {
  members: Member[] = [];
  subscription: Subscription;

  constructor(
    private dashboardService: DashboardService,
    private dataStorageService: DataStorageService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.subscription = this.dashboardService.membersChanged.subscribe(
      (members: Member[]) => {
        this.members = members;
      }
    );
    this.members = this.dashboardService.getMembers();
  }

  onNewMember() {
    this.router.navigate(['new'], { relativeTo: this.route });
  }

  onSaveChanges() {
    this.dataStorageService.storeMembers();
  }

  onRollback() {
    this.dataStorageService.loadMembers().subscribe();
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
