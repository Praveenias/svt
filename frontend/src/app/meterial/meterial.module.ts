import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';



@NgModule({
  declarations: [MatIconModule],
  imports: [
    CommonModule,
  ],
  exports:[MatIconModule,CommonModule]
})
export class MeterialModule { }
