import Image from "next/image";
import Link from "next/link"
export default function Home() {
  return (
    <>
      <h1 className="bg-primary text-5xl p-5 text-white mb-5"> Portfolio CMS </h1>
      <Link className="w-auto bg-primary text-white rounded-xl p-3" href="/another_page"> Click to go to the other page. </Link>
    </>
  );
}
