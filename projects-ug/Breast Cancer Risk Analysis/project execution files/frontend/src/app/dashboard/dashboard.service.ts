import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Subject } from 'rxjs';
import { HeaderService } from '../header/header.service';
import { RiskAssessmentService } from '../risk-assessment/risk-assessment.service';
import { Member } from './member.model';

@Injectable({ providedIn: 'root' })
export class DashboardService {
  membersChanged = new Subject<Member[]>();
  // startedEditing = new Subject<number>();

  email = this.headerService.email;
  private members: Member[] = [];

  constructor(
    private headerService: HeaderService,
    private riskAssessmentService: RiskAssessmentService,
    private router: Router
  ) {}

  setMembers(members: Member[]) {
    this.members = members;
    this.membersChanged.next(this.members.slice());
  }

  getMembers() {
    return this.members.slice();
  }

  getMember(index: number) {
    return this.members[index];
  }

  addMember(member: Member) {
    this.members.push(member);
    this.membersChanged.next(this.members.slice());
  }

  updateMember(index: number, newMember: Member) {
    this.members[index] = newMember;
    this.membersChanged.next(this.members.slice());
  }

  deleteMember(index: number) {
    this.members.splice(index, 1);
    this.membersChanged.next(this.members.slice());
  }

  memberToRiskAssessment(member: Member) {
    this.riskAssessmentService.setMember(member);
    this.router.navigate(['./risk_assessment']);
  }
}

// public members1: Member[] = [
//   new Member(
//     this.email,
//     'Laxmikant',
//     'Kabra',
//     new Date(1999, 10, 14),
//     'male',
//     0,
//     0,
//     58,
//     false,
//     0,
//     0,
//     false
//   ),
//   new Member(
//     this.email,
//     'Name',
//     'Surname',
//     new Date(2000, 9, 19),
//     'female',
//     15,
//     0,
//     65,
//     false,
//     0,
//     0,
//     false
//   ),
// ];
