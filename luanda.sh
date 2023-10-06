#!/bin/bash

while true; do
    # Execute o programa Python em segundo plano
    python3 funcionando.py &

    # Obtenha o PID (Process ID) do processo Python em execução
    python_pid=$!

    # Espere até que o processo Python termine
    wait $python_pid

    # Verifique o código de saída do programa Python
    exit_code=$?

    if [ $exit_code -ne 0 ]; then
        echo "O programa Python terminou com erro (código de saída: $exit_code). Reiniciando..."
        sleep 5
    else
        echo "O programa Python encerrou normalmente."
    fi
done

