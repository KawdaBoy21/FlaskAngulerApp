import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { ExamApiService } from './exams/exams-api.service';
import { Exam } from './exams/exam.model';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
    title = 'app';
    examsListSubs: Subscription;
    examsList: Exam[];
    constructor(private examsApi: ExamApiService) {
    }
    ngOnInit() {
        this.examsListSubs = this.examsApi
        .getExams()
        .subscribe(res => {
            this.examsList = res;
        },
        console.error
    );

    }
    ngOnDestroy() {
        this.examsListSubs.unsubscribe();
    }
}
