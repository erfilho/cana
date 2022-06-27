=begin
    
IFCE - Instituto Federal do Ceará - Campus Tianguá
Aluno: Francisco Erineldo Xavier Filho
Curso: Ciências da Computação - 5o Semestre
Professor: Adonias Caetano de Oliveira
Disciplina: Construção e Análise de Algoritmos

Trabalho Computacional 01 - Ordenação e Busca

Problema 3

Faça um programa que cadastre 10 números, ordene-os e em seguida encontre e mostre

I. O menor número e quantas vezes ele aparece no vetor;
II. O maior número e quantas vezes ele aparece no vetor;

Método utilizado: Counting Sort
=end

def min_value(array)
    aux = array[0]
    array.each{
        | i |
        if(i <= aux)
            aux = i
        end
    }
    return aux
end

def max_value(array)
    aux = 0
    array.each{
        | i |
        if(i >= aux)
            aux = i
        end
    }
    return aux
end

def countingSort(array)
    max = array.max
    c = Array.new(max + 1, 0)
    array.each {
        | e |
        c[e] += 1
    }

    res = Array.new(array.size)

    i = 0

    c.size.times do | num |
        c[num].times do 
            res[i] = num
            i += 1
        end
    end

    minval = min_value(res)
    maxval = max_value(res)

    puts "Array ordenado:"
    print res
    print "\n"
    puts "O menor número é #{minval}, ele aparece #{c[minval]} vezes"
    puts "O maior número é #{maxval}, ele aparece #{c[maxval]} vezes"
end

array = Array.new(10)
for i in 0...10
    array[i] = rand(3...8)
end

puts "Array gerado:"
print array
print "\n"
print countingSort(array)

print "\n"
puts "Digite os números para serem cadastrados: "
inpt = Array.new(10)
for i in 0...10
    inpt[i] = gets.chomp.to_i
end
puts "Array digitado: "
print inpt
print "\n"
print countingSort(inpt)