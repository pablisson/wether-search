export function Checkbox(props){
  return (
      <div>
        <label>
          <input type="checkbox" checked={props.value} onChange={props.onChange} />
          {props.label}
        </label>         
      </div>
  );
}
