import { Injectable, OnInit } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class HeaderService {
  public email:string;
  public uid:string;
  constructor() {}
  headerToggle = new Subject<boolean>();
  emailUpdate = new Subject<string>();

  ngOnInit() {}
}
