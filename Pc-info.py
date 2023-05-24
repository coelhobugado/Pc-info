import platform
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import speedtest

def get_system_info():
    system_info = {
        "Sistema Operacional": platform.system(),
        "Nome do Computador": platform.node(),
        "Versão do Sistema Operacional": platform.version(),
        "Arquitetura": platform.machine(),
        "Processador": platform.processor(),
        "Versão do Python": platform.python_version(),
        "Versão do Kernel": platform.uname().release
    }
    return system_info

def get_cpu_info():
    cpu_info = {
        "Cores Físicos": psutil.cpu_count(logical=False),
        "Cores Lógicos": psutil.cpu_count(logical=True),
        "Arquitetura": platform.processor(),
        "Frequência Máxima": f"{psutil.cpu_freq().max:.2f} MHz",
        "Frequência Mínima": f"{psutil.cpu_freq().min:.2f} MHz",
        "Frequência Atual": f"{psutil.cpu_freq().current:.2f} MHz",
        "Uso da CPU": f"{psutil.cpu_percent()}%"
    }
    return cpu_info

def get_memory_info():
    svmem = psutil.virtual_memory()
    total_gb = round(svmem.total / (1024 ** 3), 2)
    available_gb = round(svmem.available / (1024 ** 3), 2)
    used_gb = round(svmem.used / (1024 ** 3), 2)
    memory_info = {
        "Total de Memória": f"{total_gb} GB",
        "Memória Disponível": f"{available_gb} GB",
        "Memória em Uso": f"{used_gb} GB",
        "Porcentagem de Uso de Memória": f"{svmem.percent}%"
    }
    return memory_info

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total_gb = round(usage.total / (1024 ** 3), 2)
            used_gb = round(usage.used / (1024 ** 3), 2)
            free_gb = round(usage.free / (1024 ** 3), 2)
            partition_info = {
                "Ponto de Montagem": partition.mountpoint,
                "Tipo de Sistema de Arquivos": partition.fstype,
                "Tamanho Total": f"{total_gb} GB",
                "Espaço Utilizado": f"{used_gb} GB",
                "Espaço Livre": f"{free_gb} GB",
                "Porcentagem de Uso": f"{usage.percent}%"
            }
            disk_info[partition.device] = partition_info
        except PermissionError:
            partition_info = {
                "Ponto de Montagem": partition.mountpoint,
                "Tipo de Sistema de Arquivos": partition.fstype,
                "Tamanho Total": "Acesso Negado",
                "Espaço Utilizado": "Acesso Negado",
                "Espaço Livre": "Acesso Negado",
                "Porcentagem de Uso": "Acesso Negado"
            }
            disk_info[partition.device] = partition_info
    return disk_info

def get_network_info():
    try:
        speedtester = speedtest.Speedtest()
        speedtester.get_best_server()
        download_speed = speedtester.download() / 10**6
        upload_speed = speedtester.upload() / 10**6
        ping = speedtester.results.ping
        network_info = {
            "Velocidade de Download": f"{download_speed:.2f} Mbps",
            "Velocidade de Upload": f"{upload_speed:.2f} Mbps",
            "Ping": f"{ping:.2f} ms",
            "Endereço IP": speedtester.results.client["ip"],
            "Provedor de Internet": speedtester.results.client["isp"]
        }
    except speedtest.SpeedtestException:
        network_info = {
            "Erro": "Não foi possível obter as informações de velocidade da rede."
        }
    return network_info

def get_gpu_info():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            total_gb = round(gpu.memoryTotal / 1024, 2)
            used_gb = round(gpu.memoryUsed / 1024, 2)
            gpu_info = {
                "Nome da GPU": gpu.name,
                "Memória Total da GPU": f"{total_gb} GB",
                "Memória Usada da GPU": f"{used_gb} GB",
                "Uso da GPU": f"{gpu.load*100:.2f}%"
            }
        else:
            gpu_info = {
                "Erro": "Nenhuma placa de vídeo encontrada."
            }
    except ImportError:
        gpu_info = {
            "Erro": "O pacote GPUtil não está instalado."
        }
    return gpu_info

def create_table(title, data):
    table = Table(show_header=True, header_style="bold", title=title)
    table.add_column("Item", style="cyan")
    table.add_column("Valor", justify="right")
    for key, value in data.items():
        table.add_row(str(key), str(value))
    return table

def main():
    console = Console()

    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    network_info = get_network_info()
    gpu_info = get_gpu_info()

    system_table = create_table("Informações do Sistema", system_info)
    cpu_table = create_table("Informações da CPU", cpu_info)
    memory_table = create_table("Informações de Memória", memory_info)
    disk_table = create_table("Informações do Disco", disk_info)
    network_table = create_table("Informações de Rede", network_info)
    gpu_table = create_table("Informações da GPU", gpu_info)

    console.print(Panel(system_table, title="Informações do Sistema", border_style="green"))
    console.print(Panel(cpu_table, title="Informações da CPU", border_style="green"))
    console.print(Panel(memory_table, title="Informações de Memória", border_style="green"))
    console.print(Panel(disk_table, title="Informações do Disco", border_style="green"))
    console.print(Panel(network_table, title="Informações de Rede", border_style="green"))
    console.print(Panel(gpu_table, title="Informações da GPU", border_style="green"))

if __name__ == "__main__":
    main()
