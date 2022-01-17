// ConsoleApplication3.cpp : Diese Datei enthält die Funktion "main". Hier beginnt und endet die Ausführung des Programms.
//

/*
2. Učitajte niz od 10 cjelobrojinih elemenata. Ispišite aritmetičku sredinu najmanjeg i najvećeg
elementa niza, ali za izračun aritmetičke sredine definirajte funkciju arSredina.

3. U glavnom programu učitaj matricu dimenzije 3 retka i 4 stupca. Korištenjem funkcije sum_mat()
izračunajte sumu svih elemenata matrice.

4. Napišite program koji s tipkovnice učitava riječ (niz od max. 50 velikih slova abecede) te ispisuje
koliko riječ ima samoglasnika. Definirajte funkciju brojiSamoglasnike() za brojanje samoglasnika u
riječi.

5. Definirajte 3 funkcije:
Prva neka izračunava aritmetičku sredinu dva cijela broja.
Druga funkcija neka izdvaja najveći element niza.
Treća funkcija neka izdvaja najmanji element niza.
Zatim, u glavnom dijelu programa učitajte niz od 10 cjelobrojnih elemenata, te ispišite aritmetičku
sredinu najmanjeg i najvećeg elementa niza, izračunavanjem vrijednosti pomoću prethodno
definiranih funkcija.

6. Neka korisnik unese 10 cjelobrojnih elemenata niza. U funkciji izračunajte koliko je elemenata veće
od aritmetičke sredine niza. Rezultat ispišite u glavnom dijelu programa.


*/
#include <stdio.h>
#include <iostream>
#define N 3

void swap(int* xp, int* yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

void main() {

	// 1 

	int niz[N];
	int i, max, j;
	int maxMj;

	for (int i = 0; i < N; i++) {
		scanf_s("%d", &niz[i]);
	}

	max = niz[0];
	maxMj = 0;


	for (i = 0; i < N - 1; i++) {
		maxMj = i;
		for (j = i + 1; j < N; j++)
			if (niz[j] > niz[maxMj])
				maxMj = j;

		swap(&niz[maxMj], &niz[i]);
	}

	printf("\n");
	for (int i = 0; i < N; i++) {
		printf("%d\n", niz[i]);
	}

	
	// 2

	int matrix[N][N] = { {1, 2, 4}, {2, 4, 5}, {3, 6,8}};
	int row, col, temp;

	for (row = 0; row < N; row++) {
		col = row;
		temp = matrix[row][col];
		matrix[row][col] = matrix[row][(N - col) - 1];
		matrix[row][(N - col) - 1] = temp;
	}

	for (row = 0; row < N; row++) {
		for (col = 0; col < N; col++) {
			printf("%d ", matrix[row][col]);
		}
		printf("\n");
	}

}
// Programm ausführen: STRG+F5 oder Menüeintrag "Debuggen" > "Starten ohne Debuggen starten"
// Programm debuggen: F5 oder "Debuggen" > Menü "Debuggen starten"


// Tipps für den Einstieg: 
//   1. Verwenden Sie das Projektmappen-Explorer-Fenster zum Hinzufügen/Verwalten von Dateien.
//   2. Verwenden Sie das Team Explorer-Fenster zum Herstellen einer Verbindung mit der Quellcodeverwaltung.
//   3. Verwenden Sie das Ausgabefenster, um die Buildausgabe und andere Nachrichten anzuzeigen.
//   4. Verwenden Sie das Fenster "Fehlerliste", um Fehler anzuzeigen.
//   5. Wechseln Sie zu "Projekt" > "Neues Element hinzufügen", um neue Codedateien zu erstellen, bzw. zu "Projekt" > "Vorhandenes Element hinzufügen", um dem Projekt vorhandene Codedateien hinzuzufügen.
//   6. Um dieses Projekt später erneut zu öffnen, wechseln Sie zu "Datei" > "Öffnen" > "Projekt", und wählen Sie die SLN-Datei aus.
