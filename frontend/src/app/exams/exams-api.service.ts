import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import {API_URL} from '../env';
import { Exam } from './exam.model';

@Injectable()
export class ExampleService {
    constructor(private http:HttpClient) { }
    private static _handleError(err: HttpErrorResponse | any){
         return Observable.throw(err.message || 'Error: Unamble to complete the request');
    }

    getExams(): Observable<Exam[]> {
        return this.http
            .get(`${API_URL}/exams`)
            .catch(ExampleService._handleError);

    }

}
