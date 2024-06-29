import platform
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich import box
import speedtest
import GPUtil

def get_system_info():
    return {
        "Sistema Operacional": platform.system(),
        "Nome do Computador": platform.node(),
        "Versão do SO": platform.version(),
        "Arquitetura": platform.machine(),
        "Processador": platform.processor(),
        "Versão do Python": platform.python_version(),
        "Versão do Kernel": platform.uname().release
    }

def get_cpu_info():
    freq = psutil.cpu_freq()
    return {
        "Cores Físicos": psutil.cpu_count(logical=False),
        "Cores Lógicos": psutil.cpu_count(logical=True),
        "Arquitetura": platform.processor(),
        "Freq. Máxima": f"{freq.max:.2f} MHz",
        "Freq. Mínima": f"{freq.min:.2f} MHz",
        "Freq. Atual": f"{freq.current:.2f} MHz",
        "Uso da CPU": f"{psutil.cpu_percent()}%"
    }

def get_memory_info():
    svmem = psutil.virtual_memory()
    return {
        "Total": f"{svmem.total / (1024 ** 3):.2f} GB",
        "Disponível": f"{svmem.available / (1024 ** 3):.2f} GB",
        "Em Uso": f"{svmem.used / (1024 ** 3):.2f} GB",
        "Porcentagem de Uso": f"{svmem.percent}%"
    }

def get_disk_info():
    disk_info = {}
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.device] = {
                "Montagem": partition.mountpoint,
                "Sistema de Arquivos": partition.fstype,
                "Total": f"{usage.total / (1024 ** 3):.2f} GB",
                "Usado": f"{usage.used / (1024 ** 3):.2f} GB",
                "Livre": f"{usage.free / (1024 ** 3):.2f} GB",
                "Uso": f"{usage.percent}%"
            }
        except PermissionError:
            disk_info[partition.device] = {
                "Erro": "Acesso Negado"
            }
    return disk_info

def get_network_info():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 10**6
        upload_speed = st.upload() / 10**6
        ping = st.results.ping
        return {
            "Download": f"{download_speed:.2f} Mbps",
            "Upload": f"{upload_speed:.2f} Mbps",
            "Ping": f"{ping:.2f} ms",
            "IP": st.results.client["ip"],
            "ISP": st.results.client["isp"]
        }
    except speedtest.SpeedtestException:
        return {"Erro": "Falha ao obter informações de rede"}

def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu = gpus[0]
            return {
                "Nome": gpu.name,
                "Memória Total": f"{gpu.memoryTotal / 1024:.2f} GB",
                "Memória Usada": f"{gpu.memoryUsed / 1024:.2f} GB",
                "Uso": f"{gpu.load * 100:.2f}%"
            }
        else:
            return {"Erro": "GPU não encontrada"}
    except ImportError:
        return {"Erro": "GPUtil não instalado"}

def create_table(title, data, box_style=box.ROUNDED):
    table = Table(show_header=True, header_style="bold magenta", box=box_style, title=title)
    table.add_column("Item", style="cyan", no_wrap=True)
    table.add_column("Valor", style="green")
    for key, value in data.items():
        table.add_row(str(key), str(value))
    return table

def create_disk_table(disk_info, box_style=box.ROUNDED):
    table = Table(show_header=True, header_style="bold magenta", box=box_style, title="Informações do Disco")
    table.add_column("Dispositivo", style="cyan")
    table.add_column("Montagem", style="green")
    table.add_column("Sistema de Arquivos", style="yellow")
    table.add_column("Total", style="blue")
    table.add_column("Usado", style="red")
    table.add_column("Livre", style="green")
    table.add_column("Uso", style="magenta")

    for device, info in disk_info.items():
        if "Erro" in info:
            table.add_row(device, info["Erro"], "", "", "", "", "")
        else:
            table.add_row(
                device,
                info["Montagem"],
                info["Sistema de Arquivos"],
                info["Total"],
                info["Usado"],
                info["Livre"],
                info["Uso"]
            )
    return table

def main():
    console = Console()
    layout = Layout()

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
    )

    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )

    layout["header"].update(Panel(
        Text("Informações do Sistema", style="bold white on blue"),
        box=box.HEAVY,
        border_style="blue"
    ))

    layout["left"].split_column(
        Layout(name="system"),
        Layout(name="cpu"),
        Layout(name="memory"),
    )

    layout["right"].split_column(
        Layout(name="disk"),
        Layout(name="network"),
        Layout(name="gpu"),
    )

    # Obter todas as informações
    system_info = get_system_info()
    cpu_info = get_cpu_info()
    memory_info = get_memory_info()
    disk_info = get_disk_info()
    network_info = get_network_info()
    gpu_info = get_gpu_info()

    # Atualizar o layout com as informações obtidas
    layout["system"].update(Panel(create_table("Sistema", system_info), border_style="green"))
    layout["cpu"].update(Panel(create_table("CPU", cpu_info), border_style="red"))
    layout["memory"].update(Panel(create_table("Memória", memory_info), border_style="yellow"))
    layout["disk"].update(Panel(create_disk_table(disk_info), border_style="magenta"))
    layout["network"].update(Panel(create_table("Rede", network_info), border_style="cyan"))
    layout["gpu"].update(Panel(create_table("GPU", gpu_info), border_style="blue"))

    console.print(layout)

if __name__ == "__main__":
    main()
