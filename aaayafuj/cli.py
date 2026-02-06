import argparse
import sys
from aaayafuj.version import __version__
from aaayafuj.core.dispatcher import Dispatcher
from aaayafuj.core.console import InteractiveConsole

def get_parser():
    parser = argparse.ArgumentParser(
        prog='aaayafuj',
        description='Aaayafuj Cybersecurity Suite v7.0 - Professional CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Global Execution Flags
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('-s', '--server', type=str, help='Target IP address or hostname')
    parser.add_argument('-Ls', '--local-service', type=str, help='Local service port or listener')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    parser.add_argument('--yaml', action='store_true', help='Output in YAML format')
    parser.add_argument('--quiet', action='store_true', help='Suppress non-essential output')
    parser.add_argument('--verbose', action='store_true', help='Show verbose output')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('--dry-run', action='store_true', help='Simulate execution')
    parser.add_argument('--no-color', action='store_true', help='Disable colors')
    parser.add_argument('--force', action='store_true', help='Force execution')
    parser.add_argument('--timeout', type=int, help='Command timeout in seconds')

    subparsers = parser.add_subparsers(dest='category', help='Command Categories')

    # --- CORE ---
    subparsers.add_parser('status', help='Check system and engine status')
    subparsers.add_parser('uptime', help='Show engine uptime')
    subparsers.add_parser('about', help='Show tool information')
    subparsers.add_parser('license', help='Show license info')
    subparsers.add_parser('verify', help='Verify system integrity')
    subparsers.add_parser('full', help='Launch full interactive console')

    # --- PROJECT ---
    proj_p = subparsers.add_parser('project', help='Project workspace management')
    proj_sub = proj_p.add_subparsers(dest='command')
    proj_cmds = ['init', 'open', 'close', 'status', 'validate', 'build', 'deploy', 'rollback', 'backup', 'restore', 'archive', 'clean', 'lock', 'unlock', 'export', 'import']
    for cmd in proj_cmds:
        proj_sub.add_parser(cmd)

    # --- SCAN ---
    scan_p = subparsers.add_parser('scan', help='Security scanning operations')
    scan_sub = scan_p.add_subparsers(dest='command')
    scan_cmds = ['all', 'files', 'filesystem', 'permissions', 'integrity', 'hashes', 'malware', 'secrets', 'configs', 'dependencies', 'licenses', 'processes', 'services', 'startup', 'cron', 'registry', 'sudoers']
    for cmd in scan_cmds:
        scan_sub.add_parser(cmd)

    # --- NETWORK ---
    net_p = subparsers.add_parser('net', help='Network diagnostics and security')
    net_sub = net_p.add_subparsers(dest='command')
    net_cmds = ['status', 'info', 'interfaces', 'ip', 'route', 'dns', 'dns-check', 'ping', 'latency', 'traceroute', 'whois', 'firewall', 'tls-check', 'cert-info', 'proxy']
    for cmd in net_cmds:
        net_sub.add_parser(cmd)
    
    port_p = net_sub.add_parser('ports', help='Port management')
    port_sub = port_p.add_subparsers(dest='subcommand')
    port_sub.add_parser('list')
    port_sub.add_parser('open')

    # --- SYSTEM ---
    sys_p = subparsers.add_parser('sys', help='System information and health')
    sys_sub = sys_p.add_subparsers(dest='command')
    sys_cmds = ['info', 'os', 'kernel', 'uptime', 'cpu', 'memory', 'disk', 'io', 'load', 'temperature', 'power', 'processes', 'process-tree', 'services', 'startup', 'users', 'groups', 'permissions', 'environment']
    for cmd in sys_cmds:
        sys_sub.add_parser(cmd)

    # --- ASSETS ---
    assets_p = subparsers.add_parser('assets', help='Asset and file management')
    assets_sub = assets_p.add_subparsers(dest='command')
    asset_cmds = ['list', 'info', 'verify', 'hash', 'sign', 'encrypt', 'decrypt', 'compress', 'extract', 'import', 'export', 'clean', 'quarantine', 'restore']
    for cmd in asset_cmds:
        assets_sub.add_parser(cmd)

    # --- LOGS ---
    logs_p = subparsers.add_parser('logs', help='Log and audit management')
    logs_sub = logs_p.add_subparsers(dest='command')
    log_cmds = ['list', 'read', 'follow', 'search', 'errors', 'warnings', 'security', 'audit', 'export', 'rotate', 'clear']
    for cmd in log_cmds:
        logs_sub.add_parser(cmd)

    # --- SECURITY ---
    sec_p = subparsers.add_parser('sec', help='Security / Compliance')
    sec_sub = sec_p.add_subparsers(dest='command')
    sec_cmds = ['status', 'audit', 'baseline', 'hardening', 'permissions', 'policies', 'sandbox', 'compliance', 'encryption', 'integrity']
    for cmd in sec_cmds:
        sec_sub.add_parser(cmd)

    # --- USER ---
    user_p = subparsers.add_parser('user', help='User management')
    user_sub = user_p.add_subparsers(dest='command')
    user_cmds = ['list', 'info', 'add', 'remove', 'lock', 'unlock', 'roles', 'permissions', 'sessions', 'activity']
    for cmd in user_cmds:
        user_sub.add_parser(cmd)

    # --- CONFIG ---
    conf_p = subparsers.add_parser('config', help='Config management')
    conf_sub = conf_p.add_subparsers(dest='command')
    conf_cmds = ['show', 'edit', 'set', 'get', 'reset', 'validate', 'diff', 'export', 'import']
    for cmd in conf_cmds:
        conf_sub.add_parser(cmd)

    # --- UPDATE / MAINTENANCE ---
    upd_p = subparsers.add_parser('update', help='Updates and maintenance')
    upd_sub = upd_p.add_subparsers(dest='command')
    upd_cmds = ['check', 'install', 'rollback']
    for cmd in upd_cmds:
        upd_sub.add_parser(cmd)
    
    subparsers.add_parser('self-check', help='Self-diagnostic check')
    subparsers.add_parser('doctor', help='System health doctor')
    subparsers.add_parser('repair', help='Attempt auto-repair')
    subparsers.add_parser('cleanup', help='Perform system cleanup')
    subparsers.add_parser('uninstall', help='Remove Aaayafuj Suite')
    
    return parser

def main():
    parser = get_parser()
    
    if len(sys.argv) == 1:
        console = InteractiveConsole(None)
        console.start()
        sys.exit(0)

    args, unknown = parser.parse_known_args()

    if args.category == 'full':
        console = InteractiveConsole(args)
        console.start()
        sys.exit(0)

    if not args.category:
        # Check if special flags -s or -Ls are used without a category
        if args.server or args.local_service:
            print(f"[*] Quick Session: Target={args.server}, Local={args.local_service}")
            # Potentially launch a default scan or console
            console = InteractiveConsole(args)
            console.start()
            sys.exit(0)
        parser.print_help()
        sys.exit(0)

    dispatcher = Dispatcher(args)
    try:
        dispatcher.dispatch()
    except Exception as e:
        if args.debug:
            raise e
        print(f"[!] Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
