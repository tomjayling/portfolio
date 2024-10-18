program PFantasyFootball;

uses
  Vcl.Forms,
  UMain in 'UMain.pas' {MainForm},
  UGame in 'UGame.pas',
  UPlayer in 'UPlayer.pas',
  UTeam in 'UTeam.pas',
  UFormationGraphic in 'UFormationGraphic.pas' {FormationGraphicForm},
  MatchEngine in 'MatchEngine.pas' {MatchEngineForm};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TMainForm, MainForm);
  Application.CreateForm(TFormationGraphicForm, FormationGraphicForm);
  Application.CreateForm(TMatchEngineForm, MatchEngineForm);
  Application.Run;
end.
