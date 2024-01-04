export class Member {
  public email: string;
  public firstName: string;
  public lastName: string;
  public dob: Date;
  public gender: string;
  public menstrualAge: number;
  public menopausalAge: number;
  public weight: number;
  public familyHistory: boolean;
  public numberOfChild: number;
  public ageFirstChild: number;
  public maritalStatus: boolean;

  constructor(
    email: string,
    firstName: string,
    lastName: string,
    dob: Date,
    gender: string,
    menstrualAge: number,
    menopausalAge: number,
    weight: number,
    familyHistory: boolean,
    numberOfChild: number,
    ageFirstChild: number,
    maritalStatus: boolean
  ) {
    this.email = email;
    this.firstName = firstName;
    this.lastName = lastName;
    this.dob = dob;
    this.gender = gender;
    this.menstrualAge = menstrualAge;
    this.menopausalAge = menopausalAge;
    this.weight = weight;
    this.familyHistory = familyHistory;
    this.numberOfChild = numberOfChild;
    this.ageFirstChild = ageFirstChild;
    this.maritalStatus = maritalStatus;
  }
}
