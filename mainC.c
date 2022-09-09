
#include <stdio.h>
#include <stdint.h>

#include "OwnLibC.h"


typedef struct
{
	double start;
	double stop;
	uint64_t num;
}config;


int main()
{

	FILE *file;

	file = fopen("config.csv", "r");

	if (file == NULL)
	{
		printf("Error opening file. \n");
		return 1;
	}

	config conf[1];

	uint64_t read = 0;
	uint64_t records = 0;

	do{
		read = fscanf(file, "%lf, %lf, %ld\n", 
					&conf[records].start,
					&conf[records].stop,
					&conf[records].num);

		
		if (read == 3){
			records++;
		}
		else if (read != 3 && !feof(file))
		{
			printf("File format incorrect!\n");
			return 1;
		}
		else if (ferror(file)){
			printf("Error reading file.\n");
			return 1;
		}
	} while (!feof(file));
	fclose(file);

	double x[conf[0].num];
	linspace(conf[0].start, conf[0].stop, x, conf[0].num);

	for (uint64_t i = 0; i < conf[0].num; ++i)
	{
		printf("%ld, %f\n", i, x[i]);
	}

	return 0;
}