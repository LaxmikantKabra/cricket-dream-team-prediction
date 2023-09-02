import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { AssessmentResultService } from './assessment-result.service';

@Component({
  selector: 'app-assessment-result',
  templateUrl: './assessment-result.component.html',
  styleUrls: ['./assessment-result.component.css'],
})
export class AssessmentResultComponent implements OnInit, OnDestroy {
  result_message: string = 'Please perform an assessment to get a result. Please wait if you have performed assessment';
  subscription: Subscription;
  constructor(private arService: AssessmentResultService) {}

  ngOnInit(): void {
    this.subscription = this.arService.messageChanged.subscribe(
      (message: string) => {
        this.result_message = message;
        console.log(this.result_message);
      }
    );
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
