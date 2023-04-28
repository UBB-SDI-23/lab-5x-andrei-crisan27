import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Individual } from '../body/models/individuals.models';
import { AgeAvg } from '../body/models/age-statistic.models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseUrl = 'https://sdi-app-l5.strangled.net/'
  constructor(private http: HttpClient) { }

  getIndividuals(): Observable<Individual[]>{
    return this.http.get(`${this.baseUrl}restapi/individuals/`) as Observable<Individual[]>
  }

  getIndividual(individualId: number): Observable<Individual>{
    return this.http.get(`${this.baseUrl}individuals/${individualId}/`) as Observable<Individual>
  }

  getPopulationStatistic(): Observable<any> {
    return this.http.get(`${this.baseUrl}restapi/visited/sort-by-total-age/`) as Observable<any>
  }

  addIndividual(indiv: Individual): Observable<Individual>{
    return this.http.post(`${this.baseUrl}individuals/`, indiv) as Observable<Individual>
  }

  deleteIndividual(individualId: string): Observable<AgeAvg>{
    return this.http.delete(`${this.baseUrl}individuals/${individualId}/`) as Observable<AgeAvg>
  }

  updateIndividual(individualId: number, individual: Individual): Observable<Individual> {
    const url = `${this.baseUrl}individuals/${individualId}/`;
    return this.http.put<Individual>(url, individual);
  }
  
}
