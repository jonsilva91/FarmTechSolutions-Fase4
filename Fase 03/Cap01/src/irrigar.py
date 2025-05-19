def decidir_irriga(umidade: float) -> str:
    """
    Decide o status da irrigação com base na umidade.
    
    Parâmetro:
        umidade (float): valor da umidade lida

    Retorno:
        str: mensagem de status
    """
    if umidade < 65:
        return "🔴 Irrigação ATIVA (rele ligado)"
    else:
        return "🟢 Irrigação INATIVA (rele desligado)"
# Simulação do envio para o ESP32
def simular_comando_serial(umidade):
    status = decidir_irriga(umidade)
    print(f"[Simulado] Comando para o ESP32: {status}")


#Implementação serial futura

# from serial import Serial
# import time

# def enviar_comando_para_esp32(status: str):
#     """
#     Envia o comando para o ESP32 via porta serial baseado no status da irrigação.
#     Exemplo: ligar ou desligar bomba.
#     """
#     try:
#         # Substituir 'COM3' pela  porta correta e '9600' pela baudrate configurada no ESP32
#         with Serial('COM3', 9600, timeout=1) as esp:
#             time.sleep(2)  # Aguarda o ESP32 reiniciar a conexão

#             if status == "ATIVAR":
#                 esp.write(b"LIGAR\n")  # comando para ligar o relé
#             else:
#                 esp.write(b"DESLIGAR\n")  # comando para desligar o relé

#             print(f"[Serial] Comando enviado: {status}")
#     except Exception as e:
#         print("❌ Erro ao tentar enviar comando para o ESP32:")
#         import traceback; traceback.print_exc()
