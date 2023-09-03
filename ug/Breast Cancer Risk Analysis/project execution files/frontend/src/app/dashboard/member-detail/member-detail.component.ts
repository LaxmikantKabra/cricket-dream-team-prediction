import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';

import { DashboardService } from '../dashboard.service';
import { Member } from '../member.model';

@Component({
  selector: 'app-member-detail',
  templateUrl: './member-detail.component.html',
  styleUrls: ['./member-detail.component.css'],
})
export class MemberDetailComponent implements OnInit {
  member: Member;
  id: number;

  constructor(
    private dashboardService: DashboardService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params: Params) => {
      this.id = +params['id'];
      this.member = this.dashboardService.getMember(this.id);
    });
  }

  onEditMember() {
    this.router.navigate(['edit'], { relativeTo: this.route });
  }

  onDeleteMember() {
    this.dashboardService.deleteMember(this.id);
    this.router.navigate(['../'], { relativeTo: this.route });
  }

  toRiskAssessment() {
    this.dashboardService.memberToRiskAssessment(this.member);
  }
}
