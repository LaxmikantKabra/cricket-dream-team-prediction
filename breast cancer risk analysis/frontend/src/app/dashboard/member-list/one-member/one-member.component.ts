import { Component, Input, OnInit } from '@angular/core';
import { Member } from '../../member.model';

@Component({
  selector: 'app-one-member',
  templateUrl: './one-member.component.html',
  styleUrls: ['./one-member.component.css']
})
export class OneMemberComponent implements OnInit {
  @Input() member:Member;
  @Input() index:number;
  constructor() { }

  ngOnInit(): void {
  }

}
