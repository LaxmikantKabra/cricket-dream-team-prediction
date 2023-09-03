import { Component, OnDestroy, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { HeaderService } from 'src/app/header/header.service';
import { DashboardService } from '../dashboard.service';
import { Member } from '../member.model';

@Component({
  selector: 'app-member-edit',
  templateUrl: './member-edit.component.html',
  styleUrls: ['./member-edit.component.css'],
})
export class MemberEditComponent implements OnInit, OnDestroy {
  @ViewChild('f', { static: false }) editForm: NgForm;
  menopauseEncountered: boolean = false;
  familyHistWho: boolean = false;
  editIndex: number;
  editMode = false;
  editMember: Member;
  subscription: Subscription;

  firstName='';
  lastName='';
  dob:Date=null;
  gender='';
  menstrualAge: number=null;
  manopausalAge: number=null;
  weight: number=null;
  familyHistory: boolean=null;
  numberOfChild: number=null;
  ageFirstChild: number=null;
  maritalStatus:boolean = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private headerService: HeaderService,
    private dashboardService: DashboardService
  ) {}

  ngOnInit(): void {
    this.subscription = this.route.params.subscribe((params: Params) => {
      this.editIndex = +params['id'];
      this.editMode = params['id'] != null;
      if (this.editMode) {
        this.editMember = this.dashboardService.getMember(this.editIndex);
        this.firstName = this.editMember.firstName
        this.lastName = this.editMember.lastName,
        this.dob = this.editMember.dob,
        this.gender = this.editMember.gender,
        this.menstrualAge = this.editMember.menstrualAge,
        this.manopausalAge = this.editMember.menopausalAge,
        this.weight = this.editMember.weight,
        this.familyHistory = this.editMember.familyHistory,
        this.numberOfChild = this.editMember.numberOfChild,
        this.ageFirstChild = this.editMember.ageFirstChild,
        this.maritalStatus = this.editMember.maritalStatus
      }
    });
  }

  initForm() {}

  menoAgeToggleNo() {
    this.menopauseEncountered = false;
  }
  menoAgeToggleYes() {
    this.menopauseEncountered = true;
  }
  familyHistToggleYes() {
    this.familyHistWho = true;
  }
  familyHistToggleNo() {
    this.familyHistWho = false;
  }

  onClear() {
    this.editForm.reset();
  }
  onCancel() {
    this.router.navigate(['../'], { relativeTo: this.route });
  }

  onSubmit(form: NgForm) {
    const value = form.value;
    const newMember = new Member(
      this.headerService.email,
      value.firstName,
      value.lastName,
      new Date(value.dob),
      value.gender,
      value.menstrualAge,
      value.menopausalAge,
      value.weight,
      value.familyHistory,
      value.numberOfChild,
      value.ageFirstChild,
      value.maritalStatus
    );
    if (this.editMode) {
      this.dashboardService.updateMember(this.editIndex, newMember);
    } else {
      this.dashboardService.addMember(newMember);
      this.editMode = false;
      form.reset();
    }
    this.onCancel();
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
