import { Injectable, OnInit } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AssessmentResultService implements OnInit {
  isLoading: boolean = false;
  constructor() {}

  messageChanged = new Subject<string>();
  ngOnInit() {}

  displayResult(message) {
    const result_message = message;
    console.log(result_message, 'now messages changed emitted');
    this.messageChanged.next(result_message);
    // this.arComponent.isLoading = false;
  }
}
