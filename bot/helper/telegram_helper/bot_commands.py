#!/usr/bin/env python3
from bot import CMD_SUFFIX


class _BotCommands:
    def __init__(self):
        self.StartCommand       = 'start'
        self.MirrorCommand      = [f'mirror1{CMD_SUFFIX}',    f'm1{CMD_SUFFIX}']
        self.QbMirrorCommand    = [f'qbmirror1{CMD_SUFFIX}',  f'qbm1{CMD_SUFFIX}']
        self.YtdlCommand        = [f'ytdl1{CMD_SUFFIX}',      f'yt1{CMD_SUFFIX}']
        self.LeechCommand       = [f'leech1{CMD_SUFFIX}',     f'l1{CMD_SUFFIX}']
        self.QbLeechCommand     = [f'qbleech1{CMD_SUFFIX}',   f'qbl1{CMD_SUFFIX}']
        self.YtdlLeechCommand   = [f'ytdlleech1{CMD_SUFFIX}', f'ytl1{CMD_SUFFIX}']
        self.CancelAllCommand   = [f'cancelall{CMD_SUFFIX}', 'cancelallbot']
        self.RestartCommand     = [f'restart1{CMD_SUFFIX}',   'restartall']
        self.StatusCommand      = [f'status1{CMD_SUFFIX}',    'sall']
        self.PingCommand        = [f'ping{CMD_SUFFIX}',      'p']
        self.StatsCommand       = [f'stats1{CMD_SUFFIX}',     's']
        self.CloneCommand       = f'clone1{CMD_SUFFIX}'
        self.CountCommand       = f'count{CMD_SUFFIX}'
        self.DeleteCommand      = f'del{CMD_SUFFIX}'
        self.CancelMirror       = f'abort1{CMD_SUFFIX}'
        self.ListCommand        = f'list1{CMD_SUFFIX}'
        self.SearchCommand      = f'search1{CMD_SUFFIX}'
        self.UsersCommand       = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand   = f'authorize{CMD_SUFFIX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_SUFFIX}'
        self.AddSudoCommand     = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand      = f'rmsudo{CMD_SUFFIX}'
        self.HelpCommand        = f'help1{CMD_SUFFIX}'
        self.LogCommand         = f'log{CMD_SUFFIX}'
        self.ShellCommand       = f'shell{CMD_SUFFIX}'
        self.EvalCommand        = f'eval{CMD_SUFFIX}'
        self.ExecCommand        = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand      = f'bsetting1{CMD_SUFFIX}'
        self.UserSetCommand     = f'usetting1{CMD_SUFFIX}'
        self.BtSelectCommand    = f'btsel{CMD_SUFFIX}'
        self.RssCommand         = f'rss{CMD_SUFFIX}'
        self.CategorySelect     = f'catsel{CMD_SUFFIX}'
        self.RmdbCommand        = f'rmdb{CMD_SUFFIX}'
        self.RmalltokensCommand = f'rmat{CMD_SUFFIX}'

BotCommands = _BotCommands()
