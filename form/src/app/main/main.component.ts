import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { DataService } from './../../data.service';

@Component({
  selector: 'main',
  templateUrl: './novo-produto.component.html',
  styleUrls: ['./novo-produto.component.css']
})
export class NovoProdutoComponent implements OnInit {

  constructor(private service: DataService, private rota: Router) { }

  novoProduto: any = {
    name: null,
    price: null,
    sku: null
  };
  formSubmit = false;

  ngOnInit(): void {
  }
  onSubmit = (form)  => {
    this.service.post(this.novoProduto).subscribe(sucess => this.alertarOk(), error => this.alertarErro());
    setTimeout(this.onChangeRoute, 1000 * 3);
    this.formSubmit = true;

  }
  onChangeRoute = () => {
    this.rota.navigate(['/']);
  }
  alertarOk = () => {
    alert(`O Produto ${this.novoProduto.name} com valor ${this.novoProduto.price.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'})}. Foi criado com sucesso`);
  }
  alertarErro = () => {
    alert('Produto Não Cadastrado');
  }

}
