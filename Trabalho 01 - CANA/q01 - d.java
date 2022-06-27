
/*
d) PROBLEMA 04: 
    Usando uma linguagem de programação orientada a objetos como Java ou C++, implemente uma classe Aluno de atributos nome (String), nota1 e nota2 (float ou double). 
    Os atributos são privados e há métodos get/set para cada atributo. 
    Depois faça um programa que cadastre 8 alunos em array. Para cada aluno devem ser cadastrados: nome, nota1 e nota2. 
    Usando três métodos deordenação diferentes, liste todos os dados dos alunos das seguintes formas:

    I. Em ordem crescente de média ponderada das notas, tendo a primeira nota peso 2 e a segunda peso 3. 
    II. Em ordem crescente pela nota 1. 
    III. Finalmente, considerando que para ser aprovado o aluno dever ter no mínimo média 7 liste, em ordem alfabética, os alunos reprovados.
 */

class Aluno{
    private String nome;
    private double nota1;
    private double nota2;

    public Aluno(String nome, Double nota1, Double nota2) {
    this.nome = nome;
    this.nota1 = nota1;
    this.nota2 = nota2;
    }
  
    public Aluno(){
    }

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getNome() {
		return nome;
	}

    public void setnota1(Double nota1) {
		this.nota1 = nota1;
	}

	public Double getnota1() {
		return nota1;
	}

    public void setnota2(Double nota2) {
		this.nota2 = nota2;
	}

	public Double getnota2() {
		return nota2;
	}

	public Double mediaPonderada(double n1, double n2){
		double M = ((n1 * 2) + (n2 * 3))/5;
		return M;
	}

	public boolean reprovado(double media){
		if(media >= 7.0){
			return false;
		}else return true;
	}

	public Double[] ordenador_tipo_insertionSort(Double v[], int n){
		int i, j;
		double x;
		for(i = 1; i < n; i++) {
			x = v[i];
			j = i - 1;
		
		while(j >= 0 && v[j] > x) {
			v[j+1] = v[j];
			j--;
		}
		v[j+1] = x;
		}
		return v;
	}

	public String[] ordenador_tipo_selectionSort(String v[], int n){
		int i, j, min;
		String aux;

		for(i = 0; i < n-1; i++) {
			min = i;
			for(j = i+1; j < n; j++){
				if(v[j].compareTo(v[min]) < 0){
					min = j;
					aux = v[i]; v[i] = v[min]; v[min] = aux;
				}
			}
		}
		return v;
	}

	public Double[] ordenador_tipo_quickSort(Double[] vetor, int inicio, int fim) {
	
		if (inicio < fim){
			int posicaoPivo = separador(vetor, inicio, fim);
			ordenador_tipo_quickSort(vetor, inicio, posicaoPivo - 1);
			ordenador_tipo_quickSort(vetor, posicaoPivo + 1, fim);
		}
		return vetor;
  	}

  	public int separador(Double[] vetor, int inicio, int fim){
        Double pivot = vetor[inicio], aux1;
        int i = inicio + 1, f = fim;

		while(i <= f){
			if(vetor[i] <= pivot){
				i++;
			}else if(pivot < vetor[f]){
				f--;
			}else{
				aux1 = vetor[i];
				vetor[i] = vetor[f];
				vetor[f] = aux1;
				i++;
				f--;
			}
		}
		vetor[inicio] = vetor[f];
		vetor[f] = pivot;
		return f;
	}

}

public class d{
    public static void main(String[] args){
        int quant_reprovados = 0;

        Aluno[] alunos = new Aluno[8];
        Double medias[] = new Double[alunos.length];
        Double media_ordenada[] = new Double[alunos.length];
        Double notas_1_ordenada[] = new Double[alunos.length];  

        String lista_nome[] = {"Benjamin", "João", "Vitor", "Luiz", "Guilherme", "Pedro", "Alice", "Yasmin"};
        Double nota1[] = {3.5,  1.3,  9.8,  7.0,  3.7,  5.4,  6.1,  6.2};
        Double nota2[] = {8.9,  7.3,  7.2,  7.8,  2.2,  9.1,  3.6,  1.9};
        
        for(int i = 0; i < alunos.length; i++){
           alunos[i] = new Aluno(lista_nome[i], nota1[i], nota2[i]);
        }
        
        for(int i = 0; i < alunos.length; i++){
           medias[i] = alunos[i].mediaPonderada(alunos[i].getnota1(), alunos[i].getnota2());
        }

        for(int i = 0; i < alunos.length; i++){
            if(alunos[0].reprovado(medias[i]) == true){
                quant_reprovados++;
            }  
        }

        String reprovados[] = new String[quant_reprovados];
        String reprovados_ordenados[] = new String[quant_reprovados];

        int contador = 0;
            for(int i = 0; i < alunos.length; i++){
                if(alunos[0].reprovado(medias[i]) == true){
                    reprovados[contador] = alunos[i].getNome();
                    contador++;
                }  
            }

        media_ordenada = alunos[0].ordenador_tipo_insertionSort(medias, alunos.length);
        reprovados_ordenados = alunos[0].ordenador_tipo_selectionSort(reprovados, quant_reprovados);
        notas_1_ordenada = alunos[0].ordenador_tipo_quickSort(nota1, 0, alunos.length-1);

        System.out.print("Médias ordenadas: ");
        for(int i = 0; i < alunos.length; i++){
           System.out.printf("%.1f, ", media_ordenada[i]);
        }
        System.out.printf("\n");

        System.out.print("Notas 1 ordenadas: ");
        for(int i = 0; i < alunos.length; i++){
           System.out.printf("%.1f, ", notas_1_ordenada[i]);
        }
        System.out.printf("\n");
 
        System.out.print("Reprovados Ordenados Alfabeticamente: ");
        for(int i = 0; i < quant_reprovados; i++){
           System.out.printf("%s, ", reprovados_ordenados[i]);
        }
        System.out.printf("\n");
    
    }
}