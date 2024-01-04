import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable } from 'rxjs';

import { AssessmentResultService } from '../assessment-result/assessment-result.service';
import { Member } from '../dashboard/member.model';
import { RiskAssessmentService } from './risk-assessment.service';

@Component({
  selector: 'app-risk-assessment',
  templateUrl: './risk-assessment.component.html',
  styleUrls: ['./risk-assessment.component.css'],
})
export class RiskAssessmentComponent implements OnInit {
  @ViewChild('f', { static: false }) assessForm: NgForm;
  menopauseEncountered: boolean = false;
  familyHistWho: boolean = false;
  assessMember: Member;
  isMember: boolean = false;

  firstName = '';
  lastName = '';
  age: number = null;
  gender = '';
  menstrualAge: number = null;
  menopausalAge: number = null;
  weight: number = null;
  familyHistory: boolean = null;
  numberOfChild: number = null;
  ageFirstChild: number = null;
  maritalStatus: boolean = null;
  comorbodities: boolean = null;
  breastPain: boolean = null;
  cyear: number;
  by: number;
  formdata;
  constructor(
    private riskAssessmentService: RiskAssessmentService,
    private router: Router,
    private route: ActivatedRoute,
    private arservice: AssessmentResultService
  ) {}

  ngOnInit(): void {
    this.isMember = this.riskAssessmentService.isMember;
    if (this.isMember) {
      this.assessMember = this.riskAssessmentService.assessMember;
      this.firstName = this.assessMember.firstName;
      (this.lastName = this.assessMember.lastName),
        (this.cyear = +new Date().getFullYear());
      this.by = +this.assessMember.dob.getFullYear();
      this.age = this.cyear - this.by;
      // (this.dob = this.assessMember.dob),
      (this.gender = this.assessMember.gender),
        (this.menstrualAge = this.assessMember.menstrualAge),
        (this.menopausalAge = this.assessMember.menopausalAge),
        (this.weight = this.assessMember.weight),
        (this.familyHistory = this.assessMember.familyHistory),
        (this.numberOfChild = this.assessMember.numberOfChild),
        (this.ageFirstChild = this.assessMember.ageFirstChild),
        (this.maritalStatus = false);
      // console.log(this.assessMember);
    }
  }

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
  maritalStatusToggleYes() {
    this.maritalStatus = true;
  }
  maritalStatusToggleNo() {
    this.maritalStatus = false;
  }

  predictRisk(data: any) {
    data['bloodGroup'] = data.bloodGroup.toUpperCase();
    if (!data.menopausalAge) {
      const obj2 = { menopausalAge: 0 };
      Object.assign(data, obj2);
    }
    if (!data.maritalLength) {
      const obj2 = { maritalLength: 0 };
      Object.assign(data, obj2);
    }
    let riskObs: Observable<{}>;
    riskObs = this.riskAssessmentService.predictRisk(data);

    riskObs.subscribe((resData) => {
      console.log(resData);
      this.arservice.displayResult(resData);
    });
    this.router.navigate(['../assessment_result'], {
      relativeTo: this.route,
  });
  }

  onSubmit(form: NgForm) {
    this.formdata = form.form.value;
    // console.log(this.formdata);
    this.predictRisk(this.formdata);
    form.reset();
  }
}
