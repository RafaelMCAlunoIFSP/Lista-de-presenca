#include <stdio.h>
#include <string.h>

int main()
{   
    int numero,cont,total_numeros,maior,menor;
    int faixa1,faixa2,faixa3,faixa4,faixa5;
    int total_par,total_impar;
    float media;
    char decisao[1];
    cont = 0;
    while(1){
        printf("Digite um número: ");
        scanf("%i",&numero);
        
        total_numeros = total_numeros + numero;
        cont = cont + 1;
        
        if (cont == 1){
            maior = numero;
            menor = numero;
        }

        if (numero > maior){
            maior = numero ; 
        }
        if (numero < menor){
            maior = numero;
        }
        
        if (numero % 2 == 0){
            ++total_par;
        }
        else{

            ++total_impar;
        }

        if (numero < 0){
            ++faixa1;
        }
        else if (numero < 15){
                ++faixa2;
        }
        else if (numero < 100){
                ++faixa3;
        }
        else if (numero >= 1000){
                ++faixa4;
        }
        else if (numero >100 && numero < 1000){
                ++faixa5;
        }
        
        printf("Gostaria de continuar? ");
        scanf("%s",decisao);
    
        if (strcmp(decisao,"n") == 0 || strcmp(decisao,"n") == 0){
            printf("Encerrando programa... \n");
            break;
        }
        
    }
    
    printf("Total de números pares: %i \n",total_par);
    printf("Total de números ímpares: %i \n",total_impar);
    
    printf("Total de números da faixa 1: %i \n",faixa1);
    printf("Total de números da faixa 2: %i \n",faixa2);
    printf("Total de números da faixa 3: %i \n",faixa3);
    printf("Total de números da faixa 4: %i \n",faixa4);
    printf("Total de números da faixa 5: %i \n",faixa5);
    
    printf("Menor número: %i \n",menor);
    printf("Maior número: %i \n",maior);
    
    media = total_numeros / cont;
    
    printf("Média de todos os números: %.2f", media);
    
    return 0;
}